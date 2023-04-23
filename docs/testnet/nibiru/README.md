# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



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

**live-peers** (27)
```bash
peers="1e886c522cd043092062bec284e3f87a3e310b2f@45.8.133.159:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0e2fd4e31c2cb16779c4aa7c32714d1b22cb4e10@31.220.80.134:34656,595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,6ed1a9222eb38742eec37cf9a3556aa8fa5b4b18@84.46.249.197:26656,a8ce8ecbd6ce275fca632ca974f2830827d74919@183.2.149.136:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,0ca2764067c0d6a3818c95b25f73ac2769d0fd0e@45.85.249.42:26656,dc6f503fae0806a89c272bdad03f8681c25a3c75@185.182.187.2:26656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,452a3e2dda1f044221f30a8e25e6b90eaef70ce1@154.26.157.17:26656,ca91b6230e92ee6f5b9c5b1fe80fa07a1b72225a@185.211.6.205:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,8dfffa9a8da12833150a895c487b5c783ddf7d03@65.109.154.173:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,04db24e174ae43a23ad5353896764f990278b528@217.76.58.8:39656,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,acaf88fd5daa06ba52112bfb770e8ea0014c5bff@138.201.204.5:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
