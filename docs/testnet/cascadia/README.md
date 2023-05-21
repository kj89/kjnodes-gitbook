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
peers="5126c2904cf4d9ed9b2c6cd203fccbe3983229da@23.88.5.169:22656,e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,44a325485b1affd949a952811ceb76fb47f84e10@78.47.105.76:26656,4b2f6064c80803d66255a1bb322eca66f0b2036c@173.249.53.192:26656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,32bcc51674dd83a316323a67918c1cee25163291@65.109.72.12:26656,4165e807320f795900f6e590f90be16a76a7ed94@65.109.174.94:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,c94df794fdee1bf67ac7789a50159390c1580530@38.242.221.76:26656,fcac681e16636bc1185194e31d0ff9b27d7f1275@85.239.233.241:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
