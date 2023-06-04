# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/okp4.png" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v4.1.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/okp4-testnet](https://explorer.kjnodes.com/okp4-testnet)

## Public endpoints

* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)
* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* grpc: okp4-testnet.grpc.kjnodes.com:13690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:13656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (12)
```bash
peers="78d923333e39e747c6a7fbfcc822ec6279990556@91.211.251.232:28656,12367c976a54980789e56c4fcaa5c38576be9ce1@65.109.89.5:32656,a49302f8999e5a953ebae431c4dde93479e17155@15.235.46.79:26656,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,9c462b1c0ba63115bd70c3bd4f2935fcb93721d0@65.21.170.3:42656,8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,428821d6b64eee5d67da467a4673ce2b1e52955d@54.88.179.178:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
