// TODO: resolve eslint errors
/* eslint-disable turbo/no-undeclared-env-vars */
export const config = {
  NEXTAUTH_SECRET: process.env.NEXTAUTH_SECRET ?? "",
  NEXTAUTH_URL: process.env.NEXTAUTH_URL ?? "",
};
