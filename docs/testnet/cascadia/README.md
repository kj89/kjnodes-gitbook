# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

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
peers="4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,2446376d87a14585c00f74fb4eb2ccef27a2df4b@92.38.241.219:26656,d10fae49b6fa0a3dbfdca205807f79b3d53ece98@94.103.92.112:26656,cd9b30d8839e0633249ab9b5e00eb9544cdf701d@65.109.122.93:26656,4acd189e415b563c486fb6063410c23ea75f4971@38.242.139.243:55656,d09a381d3c1e93a16b508b3ba4b34765fccb1d1e@5.189.132.252:26656,a65dce99bbedee029df8558bc4471ee6cfb94dc9@38.242.229.188:26656,e80bb40ed1d6f509c21c1627ba4c14d838c71550@144.126.154.230:55656,1cfc1bef60604ad732a159b4fe69afd3dc131c73@65.109.228.9:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
