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

**live-peers** (9)
```bash
peers="0448864ede56d3c96d7d3bb8ea9f546b70cc722e@51.159.149.68:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,4ea26ce893d8f4f89a7b49b9bd77e0fbd914e029@65.109.88.162:36656,ee4c5d9a8ac7401f996ef9c4d79b8abda9505400@144.76.97.251:12656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,61544968b65e34a59513b67613519cd37ace7ecb@161.97.151.109:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656,8bccab4596e8bc162763bad6597d43523e6c32f8@104.194.8.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
