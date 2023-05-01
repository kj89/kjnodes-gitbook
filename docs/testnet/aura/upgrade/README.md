---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.5.1 | **Custom Port**: 117

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf aura
git clone https://github.com/aura-nw/aura.git
cd aura
git checkout euphoria_v0.5.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.aura/cosmovisor/upgrades/v0.5.1/bin
mv build/aurad $HOME/.aura/cosmovisor/upgrades/v0.5.1/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
