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

**live-peers** (11)
```bash
peers="8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,9928d19b7663a6fa639eb7c1ee239e671edcbdb2@5.9.147.22:26616,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,61a8b9fdd5c21ebe6c02359cb192a4eda13d44cb@135.181.139.153:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,44c4ad482cf8f1d9e7e18968da78bd0349fe853e@5.78.54.193:26656,a49302f8999e5a953ebae431c4dde93479e17155@15.235.46.79:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,14f8949ab0a276d2e55c8fa6255430881978a619@185.192.96.236:26656,428821d6b64eee5d67da467a4673ce2b1e52955d@54.88.179.178:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
