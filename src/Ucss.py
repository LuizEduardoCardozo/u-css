import HtmlParser
import cssparser

def uCss(html_text, css_text,classRegex):
    unusedCss = []

    htmlClasses = HtmlParser.parseClasses(html_text,classRegex)
    cssClasses = cssparser.getCssClasses(css_text)

    for cClass in cssClasses:
        if cClass not in htmlClasses:
            unusedCss.append(cClass)

    return unusedCss