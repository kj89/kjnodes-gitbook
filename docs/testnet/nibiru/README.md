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

**live-peers** (34)
```bash
peers="0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,7b9f7827ba8f2698167552d8045c30784a524c19@65.109.89.5:38656,595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,4dbcf74d1c5760c2ef6037219c1c9b2e7a4cea63@194.163.137.48:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,3b5c0147311c294de8e635c853af5a0de72d43f1@65.21.131.215:26566,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,7e75b2249d088a4dfc3b33f386c316cb47366d2b@195.3.221.48:11656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
