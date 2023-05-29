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
peers="275dc82c6fbea56c9c0b5098d5156a939a8698a0@178.63.102.172:25556,bc62371aa967cf2ecac4d045393a80ad92ec76f8@109.123.255.8:18656,7a9cd31ca48252a741ef0689bc35b751bffd555c@89.117.49.164:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,24c3bd618c6c6c0df40968382e6b408429a020c7@95.217.217.253:50656,c8d5ed2ce985364551b2bf11fe78770d5caafa62@82.208.22.200:26656,c4d3f14d771003d09bda04d8bd63a2a6281eab5a@185.252.233.96:26656,66e26a54afe1726bf7311e1295b4b935fb77cf24@138.124.184.134:26656,04381c060e945c9c85b31b585483f0570f36ba7c@84.54.23.199:18656,ba30fc812452dfcf0f82ccdf9c6942a1153682b0@161.97.65.105:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
