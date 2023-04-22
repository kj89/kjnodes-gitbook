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

**live-peers** (28)
```bash
peers="e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,584ca0c44e76af5484a045b22809a18587873e2d@185.196.20.33:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,15bb498412ae171d617fec5525c6be0536fa7352@94.158.152.162:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,dc6f503fae0806a89c272bdad03f8681c25a3c75@185.182.187.2:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,0ca2764067c0d6a3818c95b25f73ac2769d0fd0e@45.85.249.42:26656,c4c1285236515db8170f959433a9dc1277ba2abe@185.135.137.236:26656,28dbc46f1d5d2611b28c962d6094d03772baa7c9@217.76.50.20:26656,6ed1a9222eb38742eec37cf9a3556aa8fa5b4b18@84.46.249.197:26656,34fe5ae43d748aedcab2e6d7994f736eba32dae3@185.192.96.235:39656,452a3e2dda1f044221f30a8e25e6b90eaef70ce1@154.26.157.17:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,a33449946b9806847faf0fbb3847ddb330867d64@109.123.241.63:26656,e2a13aaf637fdce79cb90ff1a0e0567b88240bce@185.135.137.224:26656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,ca91b6230e92ee6f5b9c5b1fe80fa07a1b72225a@185.211.6.205:26656,5e8e5ca5fe3ffa7987093a91b63edc15f2e6bb4d@194.60.201.205:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,88f4766708602357ab66982bc6c48f8e34b22cfc@2.58.82.127:39656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
