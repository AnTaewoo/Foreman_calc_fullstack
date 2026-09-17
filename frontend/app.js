(function () {
  "use strict";

  const e = React.createElement;

  function Calculator() {
    const [expression, setExpression] = React.useState("");
    const [result, setResult] = React.useState("");
    const [error, setError] = React.useState("");

    function append(value) {
      setExpression(function (current) {
        return current + value;
      });
      setResult("");
      setError("");
    }

    function clear() {
      setExpression("");
      setResult("");
      setError("");
    }

    async function calculate(event) {
      if (event) {
        event.preventDefault();
      }

      if (!expression.trim()) {
        setError("Enter an expression to calculate.");
        setResult("");
        return;
      }

      setError("");

      try {
        const response = await fetch("/api/calculate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ expression: expression })
        });
        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.error || "Unable to calculate expression.");
        }

        setResult(String(data.result));
      } catch (requestError) {
        setResult("");
        setError(requestError.message || "Unable to calculate expression.");
      }
    }

    const numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."];
    const operations = ["+", "-", "*", "/", "%", "**", "(", ")"];

    return e(
      "section",
      { className: "calculator", "aria-labelledby": "calculator-title" },
      e("h1", { id: "calculator-title" }, "Calculator"),
      e(
        "form",
        { onSubmit: calculate },
        e("label", { htmlFor: "expression" }, "Expression"),
        e("input", {
          id: "expression",
          name: "expression",
          type: "text",
          value: expression,
          onChange: function (event) {
            setExpression(event.target.value);
            setResult("");
            setError("");
          },
          placeholder: "Enter an expression",
          autoComplete: "off",
          spellCheck: "false",
          "aria-describedby": "expression-help"
        }),
        e(
          "p",
          { id: "expression-help", className: "help-text" },
          "Use numbers, operators, and parentheses."
        ),
        e(
          "div",
          { className: "button-grid", "aria-label": "Calculator controls" },
          numbers.map(function (number) {
            return e(
              "button",
              {
                key: "number-" + number,
                type: "button",
                onClick: function () {
                  append(number);
                }
              },
              number
            );
          }),
          operations.map(function (operation) {
            return e(
              "button",
              {
                key: "operation-" + operation,
                type: "button",
                className: "operator",
                onClick: function () {
                  append(operation);
                },
                "aria-label": "Insert " + operation
              },
              operation
            );
          })
        ),
        e(
          "div",
          { className: "actions" },
          e(
            "button",
            { type: "button", className: "secondary", onClick: clear },
            "Clear"
          ),
          e(
            "button",
            { type: "submit", className: "primary" },
            "Calculate"
          )
        )
      ),
      result
        ? e(
            "p",
            { className: "result", role: "status" },
            e("strong", null, "Result: "),
            result
          )
        : null,
      error
        ? e(
            "p",
            { className: "error", role: "alert" },
            error
          )
        : null
    );
  }

  const rootElement = document.getElementById("root");
  ReactDOM.createRoot(rootElement).render(e(Calculator));
})();
