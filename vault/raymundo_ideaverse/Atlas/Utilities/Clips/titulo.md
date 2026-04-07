---
up: []
related: []
created: 2026-04-07
---

# titulo

Usage: gum write [flags]

Prompt for long-form text

Flags:
  -h, --help                   Show context-sensitive help.
  -v, --version                Print the version number

      --width=0                Text area width (0 for terminal width)
                               ($GUM_WRITE_WIDTH)
      --height=5               Text area height ($GUM_WRITE_HEIGHT)
      --header=""              Header value ($GUM_WRITE_HEADER)
      --placeholder="Write something..."
                               Placeholder value ($GUM_WRITE_PLACEHOLDER)
      --prompt="┃ "            Prompt to display ($GUM_WRITE_PROMPT)
      --show-cursor-line       Show cursor line ($GUM_WRITE_SHOW_CURSOR_LINE)
      --show-line-numbers      Show line numbers ($GUM_WRITE_SHOW_LINE_NUMBERS)
      --value=""               Initial value (can be passed via stdin)
                               ($GUM_WRITE_VALUE)
      --char-limit=0           Maximum value length (0 for no limit)
      --max-lines=0            Maximum number of lines (0 for no limit)
      --[no-]show-help         Show help key binds ($GUM_WRITE_SHOW_HELP)
      --cursor.mode="blink"    Cursor mode ($GUM_WRITE_CURSOR_MODE)
      --timeout=0s             Timeout until choose returns selected element
                               ($GUM_WRITE_TIMEOUT)
      --[no-]strip-ansi        Strip ANSI sequences when reading from STDIN
                               ($GUM_WRITE_STRIP_ANSI)

Style Flags
  --base.foreground=""             Foreground Color ($GUM_WRITE_BASE_FOREGROUND)
  --base.background=""             Background Color ($GUM_WRITE_BASE_BACKGROUND)
  --cursor-line-number.foreground="7"
                                   Foreground Color
                                   ($GUM_WRITE_CURSOR_LINE_NUMBER_FOREGROUND)
  --cursor-line-number.background=""
                                   Background Color
                                   ($GUM_WRITE_CURSOR_LINE_NUMBER_BACKGROUND)
  --cursor-line.foreground=""      Foreground Color
                                   ($GUM_WRITE_CURSOR_LINE_FOREGROUND)
  --cursor-line.background=""      Background Color
                                   ($GUM_WRITE_CURSOR_LINE_BACKGROUND)
  --cursor.foreground="212"        Foreground Color
                                   ($GUM_WRITE_CURSOR_FOREGROUND)
  --cursor.background=""           Background Color
                                   ($GUM_WRITE_CURSOR_BACKGROUND)
  --end-of-buffer.foreground="0"
                                   Foreground Color
                                   ($GUM_WRITE_END_OF_BUFFER_FOREGROUND)
  --end-of-buffer.background=""    Background Color
                                   ($GUM_WRITE_END_OF_BUFFER_BACKGROUND)
  --line-number.foreground="7"     Foreground Color
                                   ($GUM_WRITE_LINE_NUMBER_FOREGROUND)
  --line-number.background=""      Background Color
                                   ($GUM_WRITE_LINE_NUMBER_BACKGROUND)
  --header.foreground="240"        Foreground Color
                                   ($GUM_WRITE_HEADER_FOREGROUND)
  --header.background=""           Background Color
                                   ($GUM_WRITE_HEADER_BACKGROUND)
  --placeholder.foreground="240"
                                   Foreground Color
                                   ($GUM_WRITE_PLACEHOLDER_FOREGROUND)
  --placeholder.background=""      Background Color
                                   ($GUM_WRITE_PLACEHOLDER_BACKGROUND)
  --prompt.foreground="7"          Foreground Color
                                   ($GUM_WRITE_PROMPT_FOREGROUND)
  --prompt.background=""           Background Color
                                   ($GUM_WRITE_PROMPT_BACKGROUND)
  --padding="0 0"                  Padding ($GUM_WRITE_PADDING)
