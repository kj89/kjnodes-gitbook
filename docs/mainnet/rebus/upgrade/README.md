---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Custom Port**: 21

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf rebus.core
git clone https://github.com/rebuschain/rebus.core.git
cd rebus.core
git checkout v0.3.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.rebusd/cosmovisor/upgrades/v0.3.0/bin
mv build/rebusd $HOME/.rebusd/cosmovisor/upgrades/v0.3.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
