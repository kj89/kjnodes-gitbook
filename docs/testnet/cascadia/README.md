# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="780b02fd73b698834c4cdd0c7d7123586b71ece1@209.38.243.102:18656,0a460700e6e087887bca7c4657e3fb1b676297fa@217.76.56.58:18656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,bce4f77a3339c033c95ae96cab73f642c4d15fd5@185.187.169.105:55656,e10667304e9a3ccdc8139e49f4e3fad7d1f9f454@89.117.51.248:18656,e2ce0b38479e04d0c358962ce610902f4a3ea24c@185.230.138.64:18656,9e7532d74929bee30a2ac1f8628aca46191684ef@194.163.156.184:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,453faeace7ca167f211007fc060e251f5b636aab@195.3.223.182:15556,b08c31354f72aabc769abc8bfd0a8ee7cd0201e5@38.242.238.112:26656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
