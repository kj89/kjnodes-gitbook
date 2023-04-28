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
peers="d92e0b73ec776965c0c8fc88dcec2ebf4c990dc5@31.220.84.138:39656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,5924de9732e1bda1e6f6cef31ca0b6cd5f5dd218@38.242.226.156:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,cf755b5d8b1c400dd003221e461d717a8535c007@83.167.103.221:26656,359ab5a45015c75b0ca847519254cb8d0aa3aa6c@65.108.206.74:26656,427cfff6caf2d3f294e1adef874b17a9047b9a0c@194.163.185.141:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,a4bc4bfb7e2af517eaef8baebf5f404a0b65f59f@217.76.51.182:10656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,345cfe2a2081fee1788ee54fbb106be4900c0294@148.251.10.110:27060,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,b9da17f4f6ae0acd79608006adf04f2929f3cdf4@149.102.136.187:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,5a63a608060c18395c4748f9230e589267207f35@183.2.149.136:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
