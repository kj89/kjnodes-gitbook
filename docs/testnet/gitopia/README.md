# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,33196fb0090d2de3671e36545d3425f641c9c0dc@65.109.70.4:41656,e53572d91ae5c25caf23b6390467d1d2978ae3b7@65.109.14.17:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,a8591524ebded3132f423771c0d91b77bdffad44@82.208.22.16:26656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,4b74a2394e9c251ca24c68e666288a5fdae78010@185.245.183.246:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
