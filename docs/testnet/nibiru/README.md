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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,3b5c0147311c294de8e635c853af5a0de72d43f1@65.21.131.215:26566,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,c1b40d056e4260a9fa9d1142af1adbeec5039599@142.132.202.50:46656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
