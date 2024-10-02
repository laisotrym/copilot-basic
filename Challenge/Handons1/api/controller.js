exports.calculate = function(req, res) {
  req.app.use(function(err, _req, res, next) {
    if (res.headersSent) {
      return next(err);
    }

    res.status(400);
    res.json({ error: err.message });
  });

  if (!req.query.operation) {
    throw new Error("Unspecified operation");
  }

  if (!req.query.operand1 ||
      !req.query.operand1.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      req.query.operand1.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid operand1: " + req.query.operand1);
  }

  if (!req.query.operand2 ||
      !req.query.operand2.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      req.query.operand2.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid operand2: " + req.query.operand2);
  }

    // TODO: Add operator
    var operations = {
      'add':      function(a, b) { return Number(a) + Number(b) },
      'subtract': function(a, b) { return Number(a) - Number(b) },
      'multiply': function(a, b) { return Number(a) * Number(b) },
      'divide':   function(a, b) { return Number(a) / Number(b) }
    };

    var operation = operations[req.query.operation];
    if (!operation) {
      throw new Error("Invalid operation: " + req.query.operation);
    }

  const operand1 = req.query.operand1;
  const operand2 = req.query.operand2;

// Generate function to check number at least 5 digits and each digit after are incremented by 1
const checkNumber = (num) => {
  num = num.toString();
  if (num.length < 5) {
    return false;
  }
  for (let i = 0; i < num.length - 1; i++) {
    if (parseInt(num[i]) + 1 !== parseInt(num[i + 1])) {
      return false;
    }
  }
  return true;
}

