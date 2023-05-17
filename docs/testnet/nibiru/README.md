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

**live-peers** (22)
```bash
peers="7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,33bae0a8e95d0adc364b5feb44a766100b927e86@91.196.164.89:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,e774ca76b7765c49e21daff712fbbc93815771ab@5.9.70.180:15662,7e75b2249d088a4dfc3b33f386c316cb47366d2b@195.3.221.48:11656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,dd58949cab9bf75a42b556d04d3a4b1bbfadd8b5@144.76.97.251:40656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
