from dataclasses import dataclass

from passlib.context import CryptContext


@dataclass
class Password:
    password_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str) -> str:
        """Hashes a given password

        :param password: A plaintext password
        :type password: str
        :returns: A hashed password using CryptContext
        :rtype: str
        """

        hashed_password = self.password_context.hash(password)
        return hashed_password

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        """Verifies a given password with its hashed equivalent

        :param plain_password: A password in plaintext
        :type password: str
        :param hashed_password: A hashed password
        :rtype: str
        :returns: A boolean value depending on whether the plain password can be verified
        :rtype: bool
        """

        return self.password_context.verify(plain_password, hashed_password)
