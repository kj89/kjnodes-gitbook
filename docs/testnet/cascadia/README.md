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
peers="e500ca28e37c1fcd7f7167a6fa35c90e8d0a78f5@185.182.184.191:26656,b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656,ed0bf599702c33b800d2bc16f7968c03a678406d@65.109.50.234:26656,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,d168ed0347f827402159efbb09906689d5e693c8@85.208.48.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,a47973f2e731fc35ea0f1e2d115b51ee77b91827@109.123.249.188:26656,7b33cb7bc9c5e6417cb40fca5a1d8352ed11630a@192.210.236.76:18656,e214c682fdaa0d692b564d1d0f4f20f24e9c0cf4@38.242.147.205:18656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
