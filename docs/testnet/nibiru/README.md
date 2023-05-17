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

**live-peers** (26)
```bash
peers="7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,3b5c0147311c294de8e635c853af5a0de72d43f1@65.21.131.215:26566,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,4dc627534292d408d9087b7d62e59a10fdf99e7f@65.109.60.19:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,2bfd18d860513e6f0f8c56d4d941b975bf825a50@173.249.7.203:36656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656,b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
