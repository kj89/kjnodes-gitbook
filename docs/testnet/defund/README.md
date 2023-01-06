# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (26)
```bash
peers="6c0024b454c7e001b98ab04692c9d616d403bb7d@176.9.146.72:40656,e22fa947cb931de73fa6b4ce58d3759dbd1c0129@164.68.103.176:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,b32e6619a1c7998519d2d38828e34ace7b773852@65.109.84.250:36656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,7ca31e50d5509104ea481869bcbe91e6883fe9d0@135.181.150.198:36656,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,3c838e2b140d36e08c406884ab75119c016c7938@159.69.217.0:18656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
