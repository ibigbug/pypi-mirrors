

if __name__ == '__main__':
    import sys
    if 'daily' in sys.argv:
        from cron import daily
        daily.run()
    elif 'sync' in sys.argv:
        from cron import pypi_mirrors
        pypi_mirrors.run()
    else:
        print('Usage: python command.py sync|daily')
