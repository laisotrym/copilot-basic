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

  res.json({ result: operation(req.query.operand1, req.query.operand2) });
};

exports.hasIncrementalDigits = function(number) {
  const numStr = number.toString();

  // trim all spaces
  numStr = numStr.replace(/\s/g, '');

  if (numStr.length <= 5) {
    return false;
  }
  
  for (let i = 0; i < numStr.length - 1; i++) {
    if (parseInt(numStr[i]) + 1 !== parseInt(numStr[i + 1])) {
      return false;
    }
  }
  return true;
}
