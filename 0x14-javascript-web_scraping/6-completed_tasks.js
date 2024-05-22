#!/usr/bin/node

const rqt = require('request');
const apUrl = process.argv[2];

rqt.get(apUrl, { json: true }, (err, rsps, rpsdata) => {
  if (err) {
    console.log(err);
    return;
  }

  const comtask = {};
  rpsdata.forEach((task) => {
    if (task.completed) {
      if (!comtask[task.userId]) {
        comtask[task.userId] = 1;
      } else {
        comtask[task.userId] += 1;
      }
    }
  });
  console.log(comtask);
});
