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
* grpc: cascadia-testnet.grpc.kjnodes.com:55090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:55656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:55659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="36ca8d32631eeb973322aec9b8a9b810d5344cd4@91.201.113.194:56656,4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,df3cd1c84b2caa56f044ac19cf0267a44f2e87da@51.79.27.11:26656,d09a381d3c1e93a16b508b3ba4b34765fccb1d1e@5.189.132.252:26656,d1469dbfc3becdf0ec1640d6812793f6d33a6eda@5.9.121.55:41956,3314288924c02fd0c983ef99cf2d1d607b620b80@46.4.90.188:26656,54ca8125692084e0db82a7352d1ce42d8e075307@85.173.112.154:22656,f78611ffa950efd9ddb4ed8f7bd8327c289ba377@65.109.108.150:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
