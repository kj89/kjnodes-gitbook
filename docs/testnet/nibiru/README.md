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

**live-peers** (42)
```bash
peers="03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,4af344bb3302bf926580f0b8ea4de9be401c3522@94.131.111.156:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,afe25edd4b7515d5f013112166e157e4289177bb@95.217.35.186:46656,4dc627534292d408d9087b7d62e59a10fdf99e7f@65.109.60.19:46656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,4dbcf74d1c5760c2ef6037219c1c9b2e7a4cea63@194.163.137.48:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
