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

**live-peers** (13)
```bash
peers="b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,6903fcc270cb5189033124fece49ce4bb4745ba0@38.242.245.13:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
