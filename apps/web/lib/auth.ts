import { AuthOptions } from "next-auth";
import { config } from "~/lib/config"

const authOptions: AuthOptions = {
  secret: config.NEXTAUTH_SECRET,
  providers: [],
};

export function isAuthenticated(): boolean {
  return true;
}

export default authOptions;
