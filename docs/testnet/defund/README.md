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

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (30)
```
peers="6c0024b454c7e001b98ab04692c9d616d403bb7d@176.9.146.72:40656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,cb503107b4135363d5ff83ff6a1a1423d8db4166@62.171.169.230:40656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,7ca31e50d5509104ea481869bcbe91e6883fe9d0@135.181.150.198:36656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,fe1fe3318b450201b19827bbdf9d5aeb9ae2b916@207.180.236.115:31656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,3c838e2b140d36e08c406884ab75119c016c7938@159.69.217.0:18656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,da2902e89d484e0e499c8acf1a9dbf5f32db5de7@95.217.214.145:26656,85279852bd306c385402185e0125dffeed36bf22@38.146.3.230:11256,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656,d3b7991e387ebfe26965fe4361bc0f27789b0aa4@38.242.153.15:40656,dc8661d36681b73cf4dfde1d68587aec88212344@154.12.225.113:40656,fb5f99d34d60511d947ee077ef33005e438d0c0f@185.202.223.160:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
