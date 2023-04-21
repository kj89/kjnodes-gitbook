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

**live-peers** (29)
```bash
peers="d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,467010d590de6aab28f95ee4403d2da3463dc203@144.91.103.115:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,6394122a8dc9f78ce4e688c2d9fbaa7ae48525bc@212.86.102.21:26656,c4c1285236515db8170f959433a9dc1277ba2abe@185.135.137.236:26656,ff136d95d1e62353cbaceb2dc34ca71ca546a157@80.65.211.188:39656,78cba0a07a93e39478a4467fed7c5c8546ec642f@154.12.234.105:26656,6dc7d395ea70340e472ab2f8fb302881ae3d481e@109.123.243.8:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,e427c8f9ba21b5f4824ed77b8670f5fcd63a3bde@183.2.149.136:26656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,ca05a8a7ce9f92b8851ec941030e0670cd4ccc00@1.52.218.176:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,ca91b6230e92ee6f5b9c5b1fe80fa07a1b72225a@185.211.6.205:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,6ed1a9222eb38742eec37cf9a3556aa8fa5b4b18@84.46.249.197:26656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,4a4d0c7e8f532f755a793ab69dc27e3df8e164d9@38.242.156.12:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
