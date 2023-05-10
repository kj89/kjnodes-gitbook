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

**live-peers** (10)
```bash
peers="b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,9c462b1c0ba63115bd70c3bd4f2935fcb93721d0@65.21.170.3:42656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,15fdc722cd49ef7676205b6ad3120a84728d948c@65.108.225.158:17656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,1e48c09a0f78070e90ed49b2e3d59f8fdc188e74@162.55.234.70:55156,ee4c5d9a8ac7401f996ef9c4d79b8abda9505400@144.76.97.251:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
