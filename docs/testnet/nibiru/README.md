# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (18)
```bash
peers="5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
