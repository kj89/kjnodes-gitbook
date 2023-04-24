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
peers="6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,9fde1f50a44cbef0dede5606fbc23e939478690f@185.252.233.57:26656,cc75e7ead6a82ccc4c218cbc5e0b1545538df582@185.250.36.53:26656,11c7655bc96c229a3d18ca3bbe7d8944ce645aab@89.117.59.191:26656,dc6f503fae0806a89c272bdad03f8681c25a3c75@185.182.187.2:26656,736c0d6962c283e49ac4b4c1d2df4e9335d9923c@38.242.145.186:26656,385e57b19ab9d142b27bd0b4db3d8d84c83947e6@77.120.115.135:39656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,315082ee9277c6ebd58f0aa94ae5321dc966827d@185.211.6.98:39656,6ab457c813d267ecfcc40d50ccbe541bb2d6a9f5@193.187.129.79:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,b80df18e2aba8024321321b117bf75933000d1c4@109.123.233.202:26656,c4c1285236515db8170f959433a9dc1277ba2abe@185.135.137.236:26656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,e3b678986ea18d95943a07ee09b331da027a9fbc@173.212.248.45:26656,f863c87c1562e1d42065ee0f61e4daef9e51aa69@84.46.251.4:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,6b69faf2cd1287de0c12e04aefcde72b6578ce40@82.208.21.249:26656,c45cde328f28c16b4da3e51c45a64c7ce0c45b1c@93.183.208.71:26656,0e2fd4e31c2cb16779c4aa7c32714d1b22cb4e10@31.220.80.134:34656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
