import click
import click_log
import logging


class ColorFormatter(logging.Formatter):
    colors = {
        "error": dict(fg="red"),
        "exception": dict(fg="red"),
        "critical": dict(fg="red"),
        "debug": dict(fg="blue"),
        "warning": dict(fg="yellow"),
    }

    def format(self, record):
        if not record.exc_info:
            level = record.levelname.lower()
            msg = record.getMessage()
            if level in self.colors:
                prefix = click.style(
                    "[{}] ".format(level.upper()), **self.colors[level]
                )
                msg = "\n".join(prefix + x for x in msg.splitlines())
            return msg
        return logging.Formatter.format(self, record)


def logger_basic_config(logger: logging.Logger) -> None:
    handler = click_log.ClickHandler()
    handler.setFormatter(ColorFormatter())
    logger.handlers = [handler]


logger = logging.getLogger("cfpm")
logger_basic_config(logger)