module.exports = {
  apps: [
    {
      name: 'signalforge-backend',
      script: 'src/main.py',
      interpreter: 'python3',
      watch: true,
    },
    {
      name: 'signalforge-frontend',
      script: 'frontend/node_modules/.bin/next',
      args: 'start',
      cwd: 'frontend',
      watch: false,
    },
  ],
};
