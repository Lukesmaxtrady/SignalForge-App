import "styled-components";

declare module "styled-components" {
  export interface DefaultTheme {
    colors: {
      primary: string;
      background: string;
      panel: string;
      sidebar: string;
      text: string;
      textSecondary: string;
      textOnPrimary: string;
      notification: string;
      danger: string;
      warning: string;
      success: string;
      info: string;
    };
    borderRadius: string;
    fontFamily: string;
  }
}
