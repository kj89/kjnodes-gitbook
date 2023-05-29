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
peers="8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,a49302f8999e5a953ebae431c4dde93479e17155@15.235.46.79:26656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,ee4c5d9a8ac7401f996ef9c4d79b8abda9505400@144.76.97.251:12656,b7e01ffbe25214f24bb42f0e805d02940a7224df@194.163.172.115:17656,8bccab4596e8bc162763bad6597d43523e6c32f8@104.194.8.68:26656,23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656,428821d6b64eee5d67da467a4673ce2b1e52955d@54.88.179.178:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
