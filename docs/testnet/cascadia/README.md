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

**live-peers** (10)
```bash
peers="f47667544d7d5b65f316ba5ab8fca2e81e8fe4f4@157.90.208.222:36656,5126c2904cf4d9ed9b2c6cd203fccbe3983229da@23.88.5.169:22656,793f9456b853f0d36e8e9636dcad5cc27a169292@91.230.110.100:26656,3124aff7052b93976636b16d1c50e82a214fd6ee@65.109.155.215:26656,c01481445ec6d3e6defa945ff1075e732efb3940@65.109.28.226:19656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,32bcc51674dd83a316323a67918c1cee25163291@65.109.72.12:26656,67f25e7edb2fb19bd2a933f5ba7a87a01312eb90@89.117.49.52:26656,e4f58a1478a79cdd43564a851f2398f657050aa8@135.181.250.24:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
