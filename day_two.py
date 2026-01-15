# %%
PATH = "/usr/local/rvm/gems/ruby-3.4.7/bin:/usr/local/rvm/gems/ruby-3.4.7@global/bin:/usr/local/rvm/rubies/ruby-3.4.7/bin:/home/codespace/.vscode-remote/data/User/globalStorage/github.copilot-chat/debugCommand:/home/codespace/.vscode-remote/data/User/globalStorage/github.copilot-chat/copilotCli:/vscode/bin/linux-x64/585eba7c0c34fd6b30faac7c62a42050bfbc0086/bin/remote-cli:/home/codespace/.local/bin:/home/codespace/.dotnet:/home/codespace/nvm/current/bin:/home/codespace/.php/current/bin:/home/codespace/.python/current/bin:/home/codespace/java/current/bin:/home/codespace/.ruby/current/bin:/home/codespace/.local/bin:/usr/local/python/current/bin:/usr/local/py-utils/bin:/usr/local/jupyter:/usr/local/oryx:/usr/local/go/bin:/go/bin:/usr/local/sdkman/bin:/usr/local/sdkman/candidates/java/current/bin:/usr/local/sdkman/candidates/gradle/current/bin:/usr/local/sdkman/candidates/maven/current/bin:/usr/local/sdkman/candidates/ant/current/bin:/usr/local/rvm/gems/default/bin:/usr/local/rvm/gems/default@global/bin:/usr/local/rvm/rubies/default/bin:/usr/local/share/rbenv/bin:/usr/local/php/current/bin:/opt/conda/bin:/usr/local/nvs:/usr/local/share/nvm/versions/node/v24.11.1/bin:/usr/local/hugo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/share/dotnet:/home/codespace/.dotnet/tools:/usr/local/rvm/bin"
print(PATH)
# %%
# I shouldn't include the environment in my repo.

# %%
PATH2 = "/workspaces/daytwostuff/venv/bin:/usr/local/rvm/gems/ruby-3.4.7/bin:/usr/local/rvm/gems/ruby-3.4.7@global/bin:/usr/local/rvm/rubies/ruby-3.4.7/bin:/home/codespace/.vscode-remote/data/User/globalStorage/github.copilot-chat/debugCommand:/home/codespace/.vscode-remote/data/User/globalStorage/github.copilot-chat/copilotCli:/vscode/bin/linux-x64/585eba7c0c34fd6b30faac7c62a42050bfbc0086/bin/remote-cli:/home/codespace/.local/bin:/home/codespace/.dotnet:/home/codespace/nvm/current/bin:/home/codespace/.php/current/bin:/home/codespace/.python/current/bin:/home/codespace/java/current/bin:/home/codespace/.ruby/current/bin:/home/codespace/.local/bin:/usr/local/python/current/bin:/usr/local/py-utils/bin:/usr/local/jupyter:/usr/local/oryx:/usr/local/go/bin:/go/bin:/usr/local/sdkman/bin:/usr/local/sdkman/candidates/java/current/bin:/usr/local/sdkman/candidates/gradle/current/bin:/usr/local/sdkman/candidates/maven/current/bin:/usr/local/sdkman/candidates/ant/current/bin:/usr/local/rvm/gems/default/bin:/usr/local/rvm/gems/default@global/bin:/usr/local/rvm/rubies/default/bin:/usr/local/share/rbenv/bin:/usr/local/php/current/bin:/opt/conda/bin:/usr/local/nvs:/usr/local/share/nvm/versions/node/v24.11.1/bin:/usr/local/hugo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/share/dotnet:/home/codespace/.dotnet/tools:/usr/local/rvm/bin"
print(f"PATH after activating virtual environment (DIFFERENT): {PATH2}")

# %%
import pandas as pd
pff_df = pd.read_csv("pff_grades.csv")
pff_df


# %%
# The Extensions menu allows you to search and install tools directly inside VS Code and shows useful information like the publisher, ratings, and install count. Extensions can be enabled per each workspace, which makes it easy to customize VS Code for specific tasks.

# %% 
# Data Wrangler provides: an interactive spreadsheet-style view of DataFrames, built-in data profiling to inspect types and missing values, and the ability to generate pandas code from transformations performed in the UI.

# %%
# Installed plotly Version: 6.5.1

#%%
# We use a requirements.txt file to list our project's dependencies and their precise versions, so it can be easily recreated on another machine.
