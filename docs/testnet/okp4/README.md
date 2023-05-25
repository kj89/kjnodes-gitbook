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
peers="8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,15fdc722cd49ef7676205b6ad3120a84728d948c@65.108.225.158:17656,c030413e39be95c397c6681639f5d48675554c0c@51.79.78.121:26646,8bccab4596e8bc162763bad6597d43523e6c32f8@104.194.8.68:26656,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,44c4ad482cf8f1d9e7e18968da78bd0349fe853e@5.78.54.193:26656,b7e01ffbe25214f24bb42f0e805d02940a7224df@194.163.172.115:17656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
