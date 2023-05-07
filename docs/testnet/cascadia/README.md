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

**live-peers** (11)
```bash
peers="275dc82c6fbea56c9c0b5098d5156a939a8698a0@178.63.102.172:25556,d1469dbfc3becdf0ec1640d6812793f6d33a6eda@5.9.121.55:41956,e5ec693f420974e252ddbb488670925cc7e3524a@37.120.191.47:60756,8c3848f0f610b6fb82e4861660162b2fdabe755b@185.193.66.217:26656,4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,783a3f911d98ad2eee043721a2cf47a253f58ea1@65.108.108.52:33656,54ca8125692084e0db82a7352d1ce42d8e075307@85.173.112.154:22656,23c3d082bd3a3102988c04085531461daa5a4b21@65.108.81.122:26656,fc698cb2ca4daff21f0e4c377503343cc72dd5eb@64.225.100.42:26656,ca229d8dc311901eccb08fe36c095c0365fa7c1d@65.21.225.10:43656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
