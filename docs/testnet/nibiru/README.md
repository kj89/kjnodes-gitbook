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

**live-peers** (29)
```bash
peers="20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,cf755b5d8b1c400dd003221e461d717a8535c007@83.167.103.221:26656,c51373e7a181c8b954d894bf356adcfe10c1c25b@89.58.16.33:36656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,62ceb0aaa166dbe32c4870e5333f7bed0c7bb288@173.249.54.158:26656,537f473770b07d81a58f23e3f99dd6543339dec2@144.91.82.221:26656,8c77970aa85235d543bfb26a47a332639dc89191@68.183.236.120:26656,5fab1bfae1bc6c24332988c84815a5f289df1449@207.180.228.190:26656,7685c50934491640cc4c082a687d4d7c140a0816@38.242.226.1:26656,7635811ac19bde0a542b76a403968ea85fa5f58a@94.250.201.202:26656,a34c137b631a8c55c4dd51bf02823ab8eedc6020@89.117.51.194:26656,eb23617a926a87c8d3451ca156a3b80affd9efb4@31.220.88.158:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,0945129df734538663010c1349f1b4f29da48687@89.117.48.176:26656,3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,96285853644bd5c35db33b033abfed598c9c10c0@75.119.130.70:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,db1deb2f4d23eb91da1d10e86562d84aaa0f9a0e@5.75.239.226:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,1d31af8dcbc5a3333eb6583f97ed6b2387d70e72@34.30.60.89:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
