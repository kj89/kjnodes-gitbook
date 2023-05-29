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

**live-peers** (11)
```bash
peers="e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
