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
peers="780b02fd73b698834c4cdd0c7d7123586b71ece1@209.38.243.102:18656,04c15c3a102a6fea54e17dc9c11280f8c7f94afd@45.91.168.78:18656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,9410da5f763b47341b3b85f510d4260e47f0ed97@5.189.144.237:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,2aa27e0a6952b333b06df43d071126de2f4ce490@185.182.185.171:26656,5e00a5323aa21b54669be868f2d2ab1e9d581207@135.181.183.62:18656,475a271d79a41a952a83e914ff3c1d59fa48e76b@5.180.186.25:18656,057f860fba435eec06d8279a7658ccddec92b444@38.242.146.74:26656,54ca8125692084e0db82a7352d1ce42d8e075307@85.173.112.154:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
