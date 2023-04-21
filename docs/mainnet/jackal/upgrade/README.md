---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.2.2 | **Custom Port**: 37

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf canine-chain
git clone https://github.com/JackalLabs/canine-chain.git
cd canine-chain
git checkout v1.2.2

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.canine/cosmovisor/upgrades/bouncybulldog/bin
mv build/canined $HOME/.canine/cosmovisor/upgrades/bouncybulldog/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
