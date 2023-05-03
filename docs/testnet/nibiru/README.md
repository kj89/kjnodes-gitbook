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

**live-peers** (33)
```bash
peers="5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,fd5d54740618e8ca6d85cae52ec2db5ea8ac8ea5@91.107.196.77:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,790d36e7ea45d6660427d4c7473bac0ef525e78a@184.174.36.119:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,2d674121d87cfd1e03654da8fda7ec9f21e46713@65.109.233.78:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,4dc627534292d408d9087b7d62e59a10fdf99e7f@65.109.60.19:46656,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
