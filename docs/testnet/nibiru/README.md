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

**live-peers** (27)
```bash
peers="fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,c1b40d056e4260a9fa9d1142af1adbeec5039599@142.132.202.50:46656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
