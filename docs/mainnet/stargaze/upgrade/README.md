---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Custom Port**: 158

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf stargaze
git clone https://github.com/public-awesome/stargaze.git
cd stargaze
git checkout v9.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.starsd/cosmovisor/upgrades/v9/bin
mv bin/starsd $HOME/.starsd/cosmovisor/upgrades/v9/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
