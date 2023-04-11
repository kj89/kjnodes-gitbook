# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (28)
```bash
peers="efc2e75111f286ca7117ce4e196bfb7ba29f0a5e@109.123.243.16:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,7d66dc16d7617f44662d18633e12cdd8975e89de@38.242.228.18:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,c99466e09ac1f38e7930ce4a2b153df77637bc7e@192.3.164.17:20356,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,b2301e13ac89cd4935113cf6837178559ce8262c@79.137.203.78:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,5d55ddb4d498af6062e6e7c0cb7a670aba9b3302@68.183.65.30:26656,a2d417c0ed6452093e3f0a606db8ab97026f8ed6@38.242.228.129:39656,b15ff5df6bea62dc567f5b628bb922a4185621b6@5.75.196.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,697c14302048b65f1e292a10632bda307cb6a149@38.242.199.224:26656,a90e889ba0e38ec25b4c329851225f4ba3ace3d3@178.159.5.181:36656,a433076e0bda0bec09153a7185bfd95f6ad92b0d@185.250.36.151:26656,c410b9daf01fed8a5b44cd51573300e67ebef998@45.150.173.240:26656,13be33412283d8c2c791256af1ce029132615fd1@84.46.254.69:26656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,549a5eb615e8560105f3801315a07c49c1804f48@158.220.98.245:26656,550b17739e555f08d3861791e9be66f9581da803@207.180.214.99:26656,c06b71535f8e7322fca06a289887da423a993da0@149.102.136.173:26656,70d0a7fc3d57a61c7222b3d9891841aede5f5238@38.242.153.80:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,991fa760ff0080cee53457951bbd541a5f73910a@185.197.250.124:26656,5a60e1978836f2ce18a3c5b9acba2341ab5270fc@185.241.151.143:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
