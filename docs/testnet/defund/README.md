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

**live-peers** (19)
```
peers="67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,85279852bd306c385402185e0125dffeed36bf22@38.146.3.230:11256,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,6f6da87deb86be8d6fe273c557955c1324f1414c@86.48.5.82:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,4758cb09f15174708880c0986bb0b57af4dc5d5d@135.181.208.169:27656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,bd90b1dd4ae3636e5f452be51b8e75ca104b5bfc@109.123.247.53:40656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,b9db73c9cac1676cd389711a18a4a64eb6ce3614@135.125.153.176:26656,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
